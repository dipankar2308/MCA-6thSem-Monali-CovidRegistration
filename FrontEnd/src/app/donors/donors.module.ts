import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DonorsListComponent } from './donors-list/donors-list.component';
import { DonorsRoutingModule } from './donors-routing/donors-routing.module';
import { MaterialModule } from "./../material/material.module";
import { FlexLayoutModule } from '@angular/flex-layout';


@NgModule({
  declarations: [
    DonorsListComponent
  ],
  imports: [
    CommonModule,
    DonorsRoutingModule,
    MaterialModule,
    FlexLayoutModule
  ]
})
export class DonorsModule { }
