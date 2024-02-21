import ui.menus as menu
import ui.reusable as reusable
import modulos.campers as sc
import modulos.notas as notas
import modulos.campusland as campus

if __name__ == '__main__':
    while (True):
        opMenu = input(menu.showMenu("home"))
        if (opMenu == "1"):
            sc.newCamper()
        elif (opMenu == "2"):
            notas.pruebaAdmision()
        elif(opMenu == "3"):
            campus.newArea()
        elif(opMenu == "4"):
            campus.newRuta()
        elif(opMenu == "5"):
            sc.matricular()
        elif(opMenu == "6"):
            notas.registrarNotas()
        elif(opMenu == "7"):
            campus.newTrainer()
        elif(opMenu == "8"):
            notas.moduloReportes()
        elif(opMenu == "9"):
            sc.delCamper()
        elif(opMenu == "10"):
            sc.editarCamper()
        elif(opMenu == "11"):
            reusable.showSuccess("Gracias Por usar el Sistema")
            break
        else:
            reusable.showError("Opcion No Valida Intentalo de Nuevo")
