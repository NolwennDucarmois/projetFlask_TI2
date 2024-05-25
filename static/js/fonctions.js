document.getElementById('btnTest').onclick = () => {
    document.getElementById('titrePage').style.color = '#4f5b4a';
    document.getElementById('intro').style.display = 'grid';
    document.getElementById('intro').style.justifyItems = 'center';
    document.getElementById('intro').style.fontSize = '25px';
    document.getElementById('intro').style.color = 'red';
}

let indexCarrousel = 0;
// pour récuperer la liste des instruments
const liste = JSON.parse(document.getElementById('imgCarrousel').dataset.images)
// récupérer l'image actuellement affichée
const actuel = document.getElementById('imgCarrousel')

// fonction pour le changement de la valeur
const changement = () => {
    actuel.src = liste[indexCarrousel].src; // prend la valeur src pour l'index
    actuel.alt = liste[indexCarrousel].alt; // prend la valeur alt pour l'index
    actuel.title = liste[indexCarrousel].title;
}
document.getElementById('precedent').onclick = () => {
    // prend la valeur de :
    // si index = 0 donc que l'image est la première de la liste,
    // on prend la dernière dans la liste
    // sinon on prend celle avant l'index actuel
    indexCarrousel = (indexCarrousel === 0) ? liste.length - 1 : indexCarrousel - 1;
    changement();
}
document.getElementById('suivant').onclick = () => {
    // prend la valeur de :
    // si index = à la dernière de la liste,
    // on prend la première
    // sinon on prend celle après l'index actuel
    indexCarrousel = (indexCarrousel === liste.length - 1) ? 0 : indexCarrousel + 1;
    changement();
}