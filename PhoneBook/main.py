import user_interface as ui
import working_with_files as wwf
import working_with_data as wwd


while True:
    option = ui.menu()
    if option == 1:
        wwd.init(ui.creating_list())
        wwd.unpacking()
        print('Сохранить как')
        wwf.record(ui.file_name(), ui.file_extension(), wwd.packing())
    if option == 2:
        wwd.init(wwf.reading(ui.file_name()))
        wwd.unpacking()
        print('Сохранить как')
        wwf.record(ui.file_name(), ui.file_extension(), wwd.packing())
    if option == 3:
        break


