function getData(path,id){
    data=fetch(`https://voiceless-karel-houssame-developper-b5a205ae.koyeb.app/${path}`,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res=> res.json())
    .then(data => {
        const datalist = document.getElementById(id);
        const obj=data.elements
        Object.values(obj).forEach(elem => {
            const option = document.createElement('option');
            option.value = elem;
            datalist.appendChild(option);
        });
    })
}
document.addEventListener("DOMContentLoaded", function () {
    getData('viles','viles');
    getData('marques','marques');
    getData('models','models');
});


