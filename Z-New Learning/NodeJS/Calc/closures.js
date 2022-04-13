function getTickets(source,destination){
    let price = 0;
    if(source=='HYD' && destination=='CHN'){
        price=1000;
    }
    else if(source=='HYD' && destination=='DEL'){
        price=5000;
    }
    return function (){
        return `Ticket from ${source}-${destination}
                Price: ${price}`
    }
}

let bookTicketCHN = getTickets('HYD','CHN');
let bookTicketDEL = getTickets('HYD','DEL');

console.log(bookTicketCHN())