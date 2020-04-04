let store = {
    state: {
        showLogin: false,
        showSignup: false,
        showPredictions: false,
        hideMap: false,
        isDone: false,


    }
}

store.state.predictions = []
let startDate = new Date();
let time = startDate.getTime();
let fifteenMinutes = 15*60*1000;
for (let i = -4; i < 5; ++i) {
    store.state.predictions.push([new Date(time+i*fifteenMinutes), Math.random()])
}

export default store;