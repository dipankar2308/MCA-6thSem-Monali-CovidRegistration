import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {

    constructor(private router: Router) { }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {

        console.log("Auth guard start");
        if (localStorage.getItem('userId') != null) {
            // logged in so return true
            console.log("Auth guard true");
            return true;
        }

        // not logged in so redirect to login page with the return url
        console.log("Auth guard end");
        this.router.navigate(['/authentication/login'], { queryParams: { returnUrl: state.url } });
        return false;
    }
}