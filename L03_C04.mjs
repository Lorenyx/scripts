import fetch from 'node-fetch';

const LINKS = [
    'https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
    'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
    'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
    'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
    'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D'
]

const VALIDATION = (clock_pts) => 'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=' + clock_pts;

async function getText(index) {
    const response = await fetch(LINKS[index]);
    const data = await response.text();

    return data;
}

let BUFFER = ''

for (let i=0; i<5; i++) {
    BUFFER += await getText(i);
}

fetch(VALIDATION(BUFFER))
    .then( resp => resp.text() )
    .then (data => console.log(data));