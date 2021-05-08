import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PatientsListComponent } from './patients-list/patients-list.component';
import { PatientsRoutingModule } from './patients-routing/patients-routing.module';
import { MaterialModule } from "./../material/material.module";


@NgModule({
  declarations: [
    PatientsListComponent
  ],
  imports: [
    CommonModule,
    PatientsRoutingModule,
    MaterialModule
  ]
})
export class PatientsModule { }
