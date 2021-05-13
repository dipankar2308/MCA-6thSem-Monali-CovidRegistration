import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../shared/authentication.service';

@Component({
  selector: 'app-landing-view',
  templateUrl: './landing-view.component.html',
  styleUrls: ['./landing-view.component.css']
})
export class LandingViewComponent implements OnInit {
  public isUserAuthenticated: boolean;

  constructor(private _authService: AuthenticationService) {
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
    var userId = localStorage.getItem('userId')
    console.log("Landing page User ID: ", userId)
    if (userId == null) {
      this.isUserAuthenticated = false;
    }
    else {
      this.isUserAuthenticated = true;
    }
  }

}
