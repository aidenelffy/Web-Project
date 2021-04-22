import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {Router} from '@angular/router';
import {LoginResponse} from '../../models';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  user: LoginResponse[] = [];
  public login = '';
  public password = '';
  public confirm = '';
  public name = '';
  public email = '';
  //
  logged = false;
  // username = '';
  // password = '';
  // emailAddress = '';
  constructor(private service: AuthService, private router: Router) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  clear() {
    this.login = '';
    this.password = '';
    this.confirm = '';
    this.name = '';
    this.email = '';
  }

  signup() {
    if (!this.login || !this.password || !this.confirm) {
      alert('Please, fill all lines!');
      this.clear();
    } else if (this.password !== this.confirm) {
      alert('Passwords do not match. Check it, please!');
    }
    this.service.postUser(this.login, this.password, this.name, this.email).subscribe(res => {
      this.user.push(res);
      console.log(this.login, this.password, this.name, this.email);
      localStorage.setItem('name', res.username);
      // localStorage.setItem('users', JSON.stringify(this.user));
      this.clear();
      this.router.navigate(['/login']);
      alert('You were successfully signed up. Now, please, log in');
    });
  }
}

