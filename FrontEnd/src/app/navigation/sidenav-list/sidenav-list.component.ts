import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/shared/authentication.service';

@Component({
  selector: 'app-sidenav-list',
  templateUrl: './sidenav-list.component.html',
  styleUrls: ['./sidenav-list.component.css']
})
export class SidenavListComponent implements OnInit {

  @Output() sidenavClose = new EventEmitter();
  public isUserAuthenticated: boolean

  constructor(private _authService: AuthenticationService, private _router: Router) { }

  ngOnInit(): void {
    this._authService.authChanged
      .subscribe(res => {
        this.isUserAuthenticationCompleted();
        console.log('User Auth SideNav suscribed authentication: ', this.isUserAuthenticated);
      })

    this.isUserAuthenticationCompleted();
    console.log('User Auth SideNav component authentication: ', this.isUserAuthenticated);
  }

  private isUserAuthenticationCompleted(): void {
    if (localStorage.getItem('userId') == null) {
      this.isUserAuthenticated = false
    }
    else {
      this.isUserAuthenticated = true;
    }
  }

  public logout = () => {
    console.log('Logout clicked');
    this._authService.logout();
    console.log('Logout navigate to home');
    this._router.navigate(['/']);
    window.location.reload();
    this.onSidenavClose();
  }

  public onSidenavClose = () => {
    this.sidenavClose.emit();
  }

}