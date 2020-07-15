function getData(){
    const response = await fetch('/search');
    const data = await response.json();
    console.log(data);
}