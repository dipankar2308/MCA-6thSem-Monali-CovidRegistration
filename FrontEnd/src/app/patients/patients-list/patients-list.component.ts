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

  public displayedColumns = ['name', 'city', 'area', 'bloodGroup', 'details', 'update', 'delete'];
  public dataSource = new MatTableDataSource<Patient>();

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

  public getAllPatients = () => {
    this.repoService.getData('patients?userId=2&username=dipankar')
      .subscribe(res => {
        res = res['patients']
        this.dataSource.data = res as Patient[];
      })
  }

}
