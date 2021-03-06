import { userForAuthentication } from './../../_interfaces/user/userForAuthentication.model';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthenticationService } from './../../shared/authentication.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {
  public loginForm: FormGroup;
  public errorMessage: string = '';
  public showError: boolean;
  private _returnUrl: string;
  constructor(private _authService: AuthenticationService, private _router: Router, private _route: ActivatedRoute) { }

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      username: new FormControl("", [Validators.required]),
      password: new FormControl("", [Validators.required])
    })
    this._returnUrl = this._route.snapshot.queryParams['returnUrl'] || '/';
  }

  public validateControl = (controlName: string) => {
    return this.loginForm.controls[controlName].invalid && this.loginForm.controls[controlName].touched
  }

  public hasError = (controlName: string, errorName: string) => {
    return this.loginForm.controls[controlName].hasError(errorName)
  }
  
  public loginUser = (loginFormValue) => {
    this.showError = false;
    const login = {... loginFormValue };
    const userForAuth: userForAuthentication = {
      username: login.username,
      password: login.password
    }
    this._authService.loginUser('user/auth/login', userForAuth)
    .subscribe(res => {
      console.log("Auth completed: ", res)
       localStorage.setItem("userId", res.memberId);
       localStorage.setItem('username', login.username);
       console.log("Auth completed local storage set");
       this._authService.sendAuthStateChangeNotification(res.success);
       this._router.navigate([this._returnUrl]);
    },
    (error) => {
      this.errorMessage = "There was an error logging in with given credentials. Please try again.";
      this.showError = true;
    })
  }
}