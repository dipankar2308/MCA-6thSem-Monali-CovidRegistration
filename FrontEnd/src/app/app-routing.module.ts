import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './error-pages/not-found/not-found.component'
import { AuthGuard } from './shared/authGuard'
import { LandingViewComponent } from './landing-view/landing-view.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent, canActivate: [AuthGuard] },
  { path: 'landing', component: LandingViewComponent },
  { path: 'patients', loadChildren: () => import('./patients/patients.module').then(m => m.PatientsModule), canActivate: [AuthGuard] },
  { path: 'donors', loadChildren: () => import('./donors/donors.module').then(m => m.DonorsModule), canActivate: [AuthGuard] },
  { path: 'authentication', loadChildren: () => import('./authentication/authentication.module').then(m => m.AuthenticationModule) },
  { path: '', redirectTo: '/landing', pathMatch: 'full' },
  { path: '404', component: NotFoundComponent },
  { path: '**', redirectTo: '/404', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule],
  declarations: [],
  providers: [AuthGuard]
})
export class AppRoutingModule { }
