export interface Post{
  id: number;
  title: string;
  body: string;
  img: string;
}

export interface Product{
  id: number;
  title: string;
  body: string;
  price: number;
  img: string;
}

export interface Furniture{
  id: number;
  img: string;
  title: string;
  body: string;
  price: number;
  img2: string;
  img3: string;
  body2: string;
  img4: string;
  body3: string;
}



export interface AuthToken {
  token: string;
  id: number;
  username: string;
  password: string;
  first_name: string;
  email: string;
  is_admin: boolean;
}



export interface LoginResponse {
  token: string;
  id: number;
  username: string;
  password: string;
  first_name: string;
  email: string;
  is_admin: boolean;
}


export interface Order {
  id: number;
  img: string;
  title: string;
  price: number;
  user_id: LoginResponse;
}

