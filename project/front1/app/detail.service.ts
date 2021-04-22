import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {AuthToken, Furniture, Order, Post, Product} from './models';
import {Observable} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class DetailService {httpOptions = {
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

  getPost1(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/api/post/post1`);
  }

  getPost2(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/api/post/post2`);
  }

  getPost3(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/api/post/post3`);
  }

  getPost4(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/api/post/post4`);
  }
  getPost5(): Observable<Post[]> {
    return this.client.get<Post[]>(`${this.BASE_URL}/api/post/post5`);
  }

  getProduct(): Observable<Product[]> {
    return this.client.get<Product[]>(`${this.BASE_URL}/api/product/`);
  }

  getProductDetail(id: number): Observable<Furniture[]> {
    return this.client.get<Furniture[]>(`${this.BASE_URL}/api/product/${id}/furniture`);
  }


  getOrders(): Observable<Order[]> {
    return this.client.get<Order[]>(`${this.BASE_URL}/api/order/`);
  }

  postOrder(product: Furniture): Observable<Order> {
    return this.client.post<Order>(`${this.BASE_URL}/api/order/`, product, this.httpOptions);
  }


  deleteOrder(order: Order | number): Observable<Order> {
    const id = typeof order === 'number' ? order : order.id;
    return this.client.delete<Order>(`http://127.0.0.1:8000/api/order/${id}`, this.httpOptions);
  }

  deleteALLOrders(): Observable<Order[]> {
    return this.client.delete<Order[]>('http://127.0.0.1:8000/api/order/', this.httpOptions);

  }

}


