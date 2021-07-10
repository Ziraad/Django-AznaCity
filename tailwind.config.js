module.exports = {
    purge: [],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                primary: '#0099ff',
                secondary: '#e9ecef',
                deepskyblue: '#00bfff'
            },
            fontFamily: {
                iransans: ['iran-sans'],
                vazir: ['vazir'],
                yekan: ['yekan-edit'],
                nastaliq: ['iran-nastaliq'],
            },
            height: {
                112: '448px',
                128: '512px',
                144: '576px',
            },
            backgroundImage: theme => ({
                'header-back': "url('../images/wave (2).svg')",
                'header-back-mobile': "url('../images/oshtrankooh1.jpg')",
                'footer-back': "url('../images/wave (3).svg')",
            })
        },

    },
    variants: {
        extend: {},
    },
    plugins: [],
}
