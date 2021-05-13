import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DonorsListComponent } from '../donors-list/donors-list.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'donors', component: DonorsListComponent }
]

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
export class DonorsRoutingModule { }
