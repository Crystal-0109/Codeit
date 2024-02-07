// https://learn.codeit.kr/api/members

// fetch('https://learn.codeit.kr/api/members/3')
//   .then((response) => response.text())
//   .then((result) => { console.log(result); });

const newMember = {
  name: 'Jerry',
  email: 'jerry@codeitmall.kr',
  department: 'engineering',
};

fetch('https://learn.codeit.kr/api/members', {
  method: 'POST',
  body: JSON.stringify(newMember),
})
  .then((response) => response.text())
  .then((result) => { console.log(result); });