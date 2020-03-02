//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'beginning_zeros',
                js: 'beginningZeros'
            }
        });
        io.start();
    }
);
