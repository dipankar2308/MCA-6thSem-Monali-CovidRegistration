import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../shared/authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-landing-view',
  templateUrl: './landing-view.component.html',
  styleUrls: ['./landing-view.component.css']
})
export class LandingViewComponent implements OnInit {
  public isUserAuthenticated: boolean;

  constructor(private _authService: AuthenticationService, private _snackBar: MatSnackBar) {
    this.userAuth();
  }

  ngOnInit(): void {
    this._authService.authChanged.subscribe(res => {
      this.userAuth();
      console.log("Auth changed Landing page: ", this.isUserAuthenticated);
    });
    this.userAuth();
    console.log("ngOnInit Auth Landing page: ", this.isUserAuthenticated);
  }

  userAuth() {
    // const { enqueueSnackbar } = useSnackbar();
    var userId = localStorage.getItem('userId')
    console.log("Landing page User ID: ", userId)
    if (userId == null) {
      this.isUserAuthenticated = false;
      this.openSnackBar('Please login first!');
    }
    else {
      this.isUserAuthenticated = true;
      this.openSnackBar('Login Successful');
    }
  }

  openSnackBar(message: string) {
    console.log("Toast from Landing page");
    this._snackBar.open(message, 'close');
  }

}
