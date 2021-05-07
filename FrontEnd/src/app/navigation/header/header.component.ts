import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  @Output() public sidenavToggle = new EventEmitter();

  ngOnInit(): void {
  }

  public onToggleSidenav = () => {
    console.log("Home clicked");
    this.sidenavToggle.emit();
  }

}
