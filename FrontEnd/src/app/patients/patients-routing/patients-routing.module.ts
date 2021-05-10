import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule, Router } from '@angular/router';
import { PatientsListComponent } from '../patients-list/patients-list.component'

const routes: Routes = [
  { path: 'patients', component: PatientsListComponent },
  { path: 'patients/details', component: PatientsListComponent }
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class PatientsRoutingModule { }
