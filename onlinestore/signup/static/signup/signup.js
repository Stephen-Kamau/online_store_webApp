function signUpCheck(){
     let password = document.getElementById("password").value;
     let cPassword = document.getElementById("cpassword").value;
     let length = password.length;
     let error = "";
     if (password == cPassword ) {
         if(length < 6){
           error += "Password is very short...<ust be 6 plus characters long";
           alert(error);
           }else{
               let redirect = document.getElementById("signupform").method = "POST";
               }
               }else {
                 error +="Password doesnt match";
                 alert(error);
                  window.location.href = "./signup/signup.html";

          }
      }
