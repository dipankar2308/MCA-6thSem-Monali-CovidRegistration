import { Component, OnInit } from '@angular/core';
import { Patient } from "./../../_interfaces/patient.model";
import { MatTableDataSource } from '@angular/material/table';
import { RepositoryService } from './../../shared/repository.service'

@Component({
  selector: 'app-patients-list',
  templateUrl: './patients-list.component.html',
  styleUrls: ['./patients-list.component.css']
})
export class PatientsListComponent implements OnInit {

  public displayedColumns = ['name', 'city', 'area', 'bloodGroup', 'update', 'delete'];
  public dataSource = new MatTableDataSource<Patient>();


  constructor(private repoService: RepositoryService) { }

  ngOnInit(): void {
    this.getAllPatients();
  }

  public getAllPatients = () => {
    this.repoService.getData('api/patients')
      .subscribe(res => {
        this.dataSource.data = res as Patient[];
      })
  }

}
