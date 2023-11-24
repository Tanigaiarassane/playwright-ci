import { test, expect } from '@playwright/test';

test('has title', async ({ request }) => {
  const resposne = await request.get('https://reqres.in/api/users?page=2');
  expect (resposne.status()).toBe(200)
});

test('Not having title title', async ({ request }) => {
  const resposne = await request.get('https://reqres.in/api/users?page=2');
  expect (resposne.status()).toBe(220)
});

/*
test('Welcome title', async ({ request }) => {
  const resposne = await request.get('https://reqres.in/api/users?page=2');
  expect (resposne.status()).toBe(200)
});
*/
