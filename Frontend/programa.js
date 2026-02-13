let  url="http://127.0.0.1:8000/sumar"
let myAPI= url + "?a=5&b=45"
async function crearPeticion(){
    let response = await fetch(myAPI);
    let datos=response.json();

}
let url2="http://127.0.0.1:8000/restar"
let myAPI2= url2 + "?a=5&b=45"
async function crearPeticion(){
    let response = await fetch(myAPI2);
    let datos=response.json();