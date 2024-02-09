function readFile_promisified(filename) {
  const p = new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf8', (error, data) => {
      if (error) {
        reject(error); // 에러 발생 시 -> rejected
      } else {
        resolve(data); // 파일 내용 읽기 완료 -> fulfilled
      }
    });
  });
  return p;
}

readFile_promisified('file1.txt')
  .then((data) => { console.log(data); return readFile_promisified('file2.txt'); })
  .then((data) => { console.log(data); return readFile_promisified('file3.txt'); })
  .then((data) => { console.log(data); })
  .catch((error) => { console.log(error); });