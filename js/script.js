/* Variable with value --> BLACK */
let pixelPen = '#000000';


/* FUNCTION #1 -- Set color*/
function setPixel(paletteColor) {
    pixelPen = paletteColor;
}

/* FUNCTION #2 -- Use and change colors */
function pixelcolor(pixelBox) {
    pixelBox.style.backgroundColor = pixelPen
}