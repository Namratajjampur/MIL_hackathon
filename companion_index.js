/*
* Entry point for the companion app
*/
import { outbox } from "file-transfer";
var url = 'https://firestore.googleapis.com/v1beta1/projects/milnew-37e66/databases/(default)/documents/0/0';

fetch(url).then(function(response) {
     return response.arrayBuffer();
   }).then(function(text) {
     console.log('Fetched data');
     //console.log(text); 
     //console.log(text.fields.mode1.stringValue);
      outbox.enqueue('abc.txt',text);
      
     
     });

console.log("Companion code started");
