const form = document.getElementById('form');
const total = document.getElementById('total');
const result= document.getElementById('result');
const back= document.getElementById('back');

form.addEventListener('submit', function (event) {
    event.preventDefault(); 
    const loading = document.getElementById('preloader');
    loading.hidden = false;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
   

    const jsonData = JSON.stringify(data);

    fetch('https://predict-voitures-dans-maroc-3as14p3tp.vercel.app', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json' ,
    },
    body: jsonData 
    }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); 
        })
        .then(data => {
             console.log(data['total']);
            // Handle the response data here

            result.hidden = false;
            total.textContent = data['total'] +" DH"; //
        })
        .catch(error => {
            total.textContent = error; 

}).finally(()=>{
        loading.hidden = true;

}

)
}
);
back.onclick = function () {
    result.hidden = true;
}
