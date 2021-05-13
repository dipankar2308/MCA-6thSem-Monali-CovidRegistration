import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Patient } from "./../../_interfaces/patient.model";
import { MatTableDataSource } from '@angular/material/table';
import { RepositoryService } from './../../shared/repository.service'
import { MatSort } from '@angular/material/sort'
import { MatPaginator } from '@angular/material/paginator';

@Component({
  selector: 'app-patients-list',
  templateUrl: './patients-list.component.html',
  styleUrls: ['./patients-list.component.css']
})
export class PatientsListComponent implements OnInit, AfterViewInit {

  public displayedColumns = ['name', 'city', 'area', 'bloodGroup', 'details', 'update'];
  public dataSource = new MatTableDataSource<Patient>();
  public isLoading = false;

  @ViewChild(MatSort) sort: MatSort;
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private repoService: RepositoryService) { }

  ngOnInit(): void {
    this.getAllPatients();
  }

  ngAfterViewInit(): void {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }

  public customSort = (param) => {
    console.log("Sorting changed on patients table", param)
  }

  public doFilter = (value: string) => {
    this.dataSource.filter = value.trim().toLocaleLowerCase();
  }

  public redirectToDetails = (memberId: string) => {
    console.log(`Details for patient id ${memberId} clicked.`)
  }

  public redirectToUpdate = (memberId: string) => {
    console.log(`Update for patient id ${memberId} clicked.`)
  }

  public getAllPatients = () => {
    this.isLoading = true;
    var userId = localStorage.getItem('userId');
    var username = localStorage.getItem('username');
    this.repoService.getData(`patients?userId=${userId}&username=${username}`)
      .subscribe(res => {
        res = res['patients']
        console.log(res);
        this.dataSource.data = res as Patient[];
        this.isLoading = false;
      })
  }

}
