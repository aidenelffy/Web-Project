import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {AuthToken, LoginResponse} from '../models';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  httpOptions = {
    headers: new HttpHeaders({'Content-Type': 'application/json'})
  };

  BASE_URL = 'http://127.0.0.1:8000';

  constructor(private client: HttpClient) {
  }


  login(username, password): Observable<AuthToken> {
    return this.client.post<AuthToken>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }



  postUser(login: any, pass: any, name: any, Email: any): Observable<AuthToken> {
    return this.client.post<LoginResponse>(`${this.BASE_URL}/api/register/`, {
      username: login,
      password: pass,
      first_name: name,
      email: Email
    }, this.httpOptions);
  }

}
