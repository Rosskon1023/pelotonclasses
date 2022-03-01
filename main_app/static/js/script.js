const dateElOne = document.getElementById('id_workoutdate');
const dateElTwo = document.getElementById('id_classdate');

M.Datepicker.init(dateElOne, dateElTwo, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: false,
    autoClose: true
});

M.Datepicker.init(dateElTwo, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: false,
    autoClose: true
});