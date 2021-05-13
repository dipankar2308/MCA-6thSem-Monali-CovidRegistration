import { CommonModule } from '@angular/common'; 
import { NgModule } from '@angular/core'; 
import { MatListModule } from '@angular/material/list';  
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';
import { LayoutComponent } from './layout/layout.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HomeComponent } from './home/home.component';
import { MatSidenavModule } from '@angular/material/sidenav';
import { HeaderComponent } from './navigation/header/header.component';
import { SidenavListComponent } from './navigation/sidenav-list/sidenav-list.component';
import { HttpClientModule } from '@angular/common/http';
import { PatientsModule } from './patients/patients.module';
import { RepositoryService } from "./shared/repository.service";
import { LoginComponent } from './authentication/login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NotFoundComponent } from './error-pages/not-found/not-found.component';
import { MenuComponent } from './menu/menu.component';
import { LandingViewComponent } from './landing-view/landing-view.component';
import { DonorsModule } from './donors/donors.module';


@NgModule({
  declarations: [
    AppComponent,
    LayoutComponent,
    HomeComponent,
    HeaderComponent,
    SidenavListComponent,
    NotFoundComponent,
    MenuComponent,
    LandingViewComponent,
  ],
  exports: [
    AppComponent
  ],
  imports: [
    CommonModule, 
    FormsModule, 
    MatListModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule,
    MatSidenavModule,
    HttpClientModule,
    PatientsModule,
    ReactiveFormsModule,
    DonorsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
