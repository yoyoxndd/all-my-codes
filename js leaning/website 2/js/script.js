document.getElementById("changeit").addEventListener("click", function() {
    let r = math.floor(math.random() * 256)
    let g = math.floor(math.random() * 256)
    let b = math.floor(math.random() * 256)

    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});