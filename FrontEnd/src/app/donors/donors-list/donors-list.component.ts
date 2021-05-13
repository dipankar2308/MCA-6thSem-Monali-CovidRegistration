import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { RepositoryService } from './../../shared/repository.service'
import { MatSort } from '@angular/material/sort'
import { MatPaginator } from '@angular/material/paginator';
import { Donor } from './../../_interfaces/donor.model'

@Component({
  selector: 'app-donors-list',
  templateUrl: './donors-list.component.html',
  styleUrls: ['./donors-list.component.css']
})
export class DonorsListComponent implements OnInit {
  public displayedColumns = ['name', 'city', 'area', 'bloodGroup', 'details', 'update'];
  public dataSource = new MatTableDataSource<Donor>();
  public isLoading = false;

  @ViewChild(MatSort) sort: MatSort;
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private _repoService: RepositoryService) { }

  ngOnInit(): void {
    this.getAllDonors();
  }

  public customSort = (param) => {
    console.log("Sorting changed on donors table", param)
  }

  public doFilter = (value: string) => {
    this.dataSource.filter = value.trim().toLocaleLowerCase();
  }

  public redirectToDetails = (memberId: string) => {
    console.log(`Donor details for id:${memberId} clicked`);
  }

  public getAllDonors = () => {
    this.isLoading = true;
    var userId = localStorage.getItem('userId');
    var username = localStorage.getItem('username');
    this._repoService.getData(`donors?userId=${userId}&username=${username}`)
      .subscribe(res => {
        res = res['donors']
        console.log(res);
        this.dataSource.data = res as Donor[];
        this.isLoading = false;
      })
  }

}
