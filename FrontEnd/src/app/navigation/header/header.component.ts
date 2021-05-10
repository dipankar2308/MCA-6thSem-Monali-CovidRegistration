import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from './../../shared/authentication.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  public isUserAuthenticated: boolean;
  constructor(private _authService: AuthenticationService, private _router: Router) {

  }

  @Output() public sidenavToggle = new EventEmitter();

  ngOnInit(): void {
    this._authService.authChanged
      .subscribe(res => {
        this.isUserAuthenticationCompleted();
        console.log('User Auth Header suscribed authentication: ', this.isUserAuthenticated);
      })

    this.isUserAuthenticationCompleted();
    console.log('User Auth Header component: ', this.isUserAuthenticated);
  }

  private isUserAuthenticationCompleted(): void {
    if (localStorage.getItem('userId') == null) {
      this.isUserAuthenticated = false
    }
    else {
      this.isUserAuthenticated = true;
    }
  }

  public onToggleSidenav = () => {
    console.log("Home clicked");
    this.sidenavToggle.emit();
  }

  public logout = () => {
    console.log('Logout clicked');
    this._authService.logout();
    console.log('Logout navigate to home');
    this._router.navigate(['/']);
    window.location.reload();
  }

}
