from rolepermissions.roles import AbstractUserRole

class Atendente(AbstractUserRole):
    available_permissions = {
        'view_orders': True,
        'send_esims_but': True,
    }
class Gerente(AbstractUserRole):
    available_permissions = {
        'view_orders': True,
        'edit_orders': True,
        'import_orders': True,
        'export_orders': True,
        'view_sims': True,
        'add_sims': True,
        'add_esims': True,
        'edit_sims': True,
        'add_ord_sims': True,
        'send_esims': True,
        'send_esims_but': True,
    }