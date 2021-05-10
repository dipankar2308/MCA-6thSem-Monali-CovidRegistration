import { Router } from '@angular/router';
import { PasswordConfirmationValidatorService } from './../../shared/custom-validators/password-confirmation-validator.service';
import { userProfile } from './../../_interfaces/user/userProfile.model';
import { userForAuthentication } from './../../_interfaces/user/userForAuthentication.model';
import { AuthenticationService } from './../../shared/authentication.service';
import { RepositoryService } from './../../shared/repository.service'
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.css']
})

export class RegisterUserComponent implements OnInit {
  public registerForm: FormGroup;
  public errorMessage: string = '';
  public showError: boolean;

  constructor(private _authService: AuthenticationService,
    // private _passConfValidator: PasswordConfirmationValidatorService,
    private _repositoryService: RepositoryService,
    private _router: Router) { }

  ngOnInit(): void {
    this.registerForm = new FormGroup({
      username: new FormControl(''),
      area: new FormControl(''),
      bloodGroup: new FormControl(''),
      city: new FormControl(''),
      name: new FormControl(''),
      phoneNumber: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required]),
      confirm: new FormControl('', [Validators.required])
    });
    // this.registerForm.get('confirm').setValidators([Validators.required, this._passConfValidator.validateConfirmPassword(this.registerForm.get('password'))]);
  }

  public validateControl = (controlName: string) => {
    return this.registerForm.controls[controlName].invalid && this.registerForm.controls[controlName].touched
  }

  public hasError = (controlName: string, errorName: string) => {
    return this.registerForm.controls[controlName].hasError(errorName)
  }

  public registerUser = (registerFormValue) => {
    this.showError = false;
    const formValues = { ...registerFormValue };

    const userForLogin: userForAuthentication = {
      username: formValues.username,
      password: formValues.userId
    }

    this._authService.registerUser("api/accounts/registration", userForLogin)
      .subscribe(_ => {
        var id = _.memberId;
        const user: userProfile = {
          username: formValues.username,
          userId: id,
          area: formValues.area,
          bloodGroup: formValues.bloodGroup,
          city: formValues.city,
          name: formValues.name,
          phoneNumber: formValues.phoneNumber
        };

        this._repositoryService.create('user/profile/'.concat(user.username), user).subscribe(res => {
          this._router.navigate(["/authentication/login"]);
        }, error => {
          this.errorMessage = error;
          this.showError = true;
        })
      },
        error => {
          this.errorMessage = error;
          this.showError = true;
        });
  }
}