import subprocess
import json
from tabulate import tabulate


def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout


def main():
    print("Iniciando sesión en Azure...")
    az_login = run_command("az login")
    if not az_login:
        print("No se pudo iniciar sesión en Azure.")
        return

    while True:
        print("Obteniendo suscripciones...")
        subscriptions = json.loads(run_command("az account list"))

        subscription_table = [[i + 1, subscription['name'], subscription['id']]
                              for i, subscription in enumerate(subscriptions)]
        print(tabulate(subscription_table, headers=["#", "Nombre", "ID"]))

        subscription_choice = int(
            input("Seleccione la suscripción (0 para salir): ")) - 1
        if subscription_choice == -1:
            break

        subscription_name = subscriptions[subscription_choice]['name']
        subscription_id = subscriptions[subscription_choice]['id']
        run_command(f"az account set --subscription {subscription_id}")

        choose_another_subscription = False
        while not choose_another_subscription:
            print("Obteniendo vnets...")
            vnets = json.loads(run_command("az network vnet list"))

            vnet_table = [[i + 1, vnet['name'], vnet['resourceGroup']]
                          for i, vnet in enumerate(vnets)]
            print(tabulate(vnet_table, headers=[
                  "#", "Nombre VNet", "Resource Group"]))

            vnet_choice = int(input("Seleccione la VNet (0 para salir): ")) - 1
            if vnet_choice == -1:
                break

            vnet_name = vnets[vnet_choice]['name']
            resource_group = vnets[vnet_choice]['resourceGroup']

            choose_another_vnet = False
            while not choose_another_vnet:

                print("Obteniendo subnets...")
                subnets = json.loads(run_command(
                    f"az network vnet subnet list --vnet-name {vnet_name} --resource-group {resource_group}"))

                subnet_table = [[i + 1, subnet['name']]
                                for i, subnet in enumerate(subnets)]
                print(tabulate(subnet_table, headers=["#", "Nombre Subnet"]))

                subnet_choice = int(
                    input("Seleccione la subnet (0 para salir): ")) - 1
                if subnet_choice == -1:
                    break

                subnet_name = subnets[subnet_choice]['name']

                print(
                    f"En la subnet '{subnet_name}', las primeras cinco IPs libres son:")
                ip_ranges = subnets[subnet_choice]['addressPrefix'].split(",")
                ips = json.loads(run_command(
                    f"az network vnet subnet list-available-ips --name {subnet_name} --vnet-name {vnet_name} --resource-group {resource_group}"))

                for ip in ips:
                    print(ip)

                print("\n¿Qué quieres hacer ahora?")
                print(f"\n1. Elegir otra suscripción")
                print(
                    f"2. Elegir otra VNet de la suscripción {subscription_name}")
                print(f"3. Elegir otra subnet de la VNet {vnet_name}")
                print("4. Salir")

                menu_choice = int(input("Seleccione una opción: "))
                if menu_choice == 1:
                    choose_another_subscription = True
                elif menu_choice == 2:
                    choose_another_vnet = True
                elif menu_choice == 3:
                    continue  # Continuar al siguiente bucle de subnet
                elif menu_choice == 4:
                    return  # Salir del programa
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            # Fin del bucle de subnet
        # Fin del bucle de VNet
    # Fin del bucle de suscripción


if __name__ == "__main__":
    main()
