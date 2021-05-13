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
  public isLoading = false;
  public bloodGroups = [];

  constructor(private _authService: AuthenticationService,
    private _passConfValidator: PasswordConfirmationValidatorService,
    private _repositoryService: RepositoryService,
    private _router: Router) { }

  ngOnInit(): void {
    this.registerForm = new FormGroup({
      username: new FormControl(''),
      area: new FormControl(''),
      bloodGroup: new FormControl('A+'),
      city: new FormControl(''),
      name: new FormControl(''),
      phoneNumber: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required]),
      confirm: new FormControl('')
    });

    this.getBloodGroups();
    this.registerForm.get('confirm').setValidators([Validators.required, this._passConfValidator.validateConfirmPassword(this.registerForm.get('password'))]);
  }

  private getBloodGroups = () => {
    this.isLoading = true;
    this._repositoryService.getBloodGroups(`data/bloodGroups`).subscribe(res => {
      if (res.success) {
        res.bloodGroups.map(group => {
          console.log(group);
          this.bloodGroups.push({ item: group, value: group });
        });
        console.log(this.bloodGroups);
      }
      this.isLoading = false;
    })
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
      password: formValues.password
    }

    this._authService.registerUser("user/auth/register", userForLogin)
      .subscribe(res => {
        if (res.success) {
          console.log("User register response: ", res);

          var id = res.memberId.toString();
          const user: userProfile = {
            username: formValues.username,
            userId: id,
            area: formValues.area,
            bloodGroup: formValues.bloodGroup,
            city: formValues.city,
            name: formValues.name,
            phoneNumber: formValues.phoneNumber
          };

          this._repositoryService.create(`user/profile/${user.username}`, user).subscribe(res => {
            this._router.navigate(["/authentication/login"]);
          }, error => {
            console.log("Error in user registration: ", error);
            this.errorMessage = error;
            this.showError = true;
          })
        }
        else {
          this.errorMessage = res.message;
          this.showError = true;
        }
      },
        error => {
          console.log("Error in user credential registration: ", error);
          this.errorMessage = error;
          this.showError = true;
        });
  }
}