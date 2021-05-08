import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PatientsListComponent } from './patients-list/patients-list.component';
import { PatientsRoutingModule } from './patients-routing/patients-routing.module';
import { MaterialModule } from "./../material/material.module";
import { FlexLayoutModule } from '@angular/flex-layout';



@NgModule({
  declarations: [
    PatientsListComponent
  ],
  imports: [
    CommonModule,
    PatientsRoutingModule,
    MaterialModule,
    FlexLayoutModule
  ]
})
export class PatientsModule { }
