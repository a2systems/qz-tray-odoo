odoo.define('qz-tray-odoo.javascript', function (require) {
        'use strict';

        $().ready(function () {

                console.log('Estamos aca');
                console.log('Texto ',$('#btn-qz-print').html());

                $("#btn-qz-close").click(function () {
                        window.close();
                });

                $("#btn-qz-print").click(function () {
                          var zpl_code_field = $('span[name="zpl_code"]').html();
                          console.log('Print label',zpl_code_field);
                          qz.websocket.connect().then(() => {
                                var printer_name_field = $('#printerName').val();
                                console.log('Printer name',printer_name_field);
                                return qz.printers.find("ZDesigner");
                          }).then((found) => {
                                 console.log(found);
                                 var num_copies_field = parseInt($('#copiesNumber').val());
                                 console.log('Copies',num_copies_field);
                                 var config = qz.configs.create(found, {copies: num_copies_field});
                                 var data = [
                                        '^XA\n',
                                        '^FO50,50^ADN,36,20^FDPRINTED USING QZ TRAY PLUGIN\n',
                                        '^FS\n',
                                        '^XZ\n'
                                 ];
                                 var zpl_code_field = $('span[name="zpl_code"]').html();
                                 console.log('ZPL',zpl_code_field);
                                 var data = [zpl_code_field];
                                 $(this).prop("disabled",true);
                                 return qz.print(config, data);
                                });

                });

        });
});
