import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {

    constructor(private router: Router, private _snackBar: MatSnackBar) { }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {

        console.log("Auth guard start");
        if (localStorage.getItem('userId') != null) {
            // logged in so return true
            console.log("Auth guard true");
            return true;
        }

        // not logged in so redirect to login page with the return url
        console.log("Auth guard end");
        this.router.navigate(['/landing'], { queryParams: { returnUrl: state.url } });
        this.openSnackBar("Please login first");
        return false;
    }

    openSnackBar(message: string) {
        console.log("Toast from Landing page");
        this._snackBar.open(message, 'close', {
            duration: 2500
        });
    }
}