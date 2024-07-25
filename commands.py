cmds = {
    'reset': {
        'cmd1': 0xFF,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'sync_reset': {
        'cmd1': 0xFC,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'reset_lun': {
        'cmd1': 0x00,
        'addr_len': 3,
        'cmd2': 0xFA,
        'data': None,
        'await_data': False
    },
    'read_device_id': {
        'cmd1': 0x90,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'read_param_page': {
        'cmd1': 0xEC,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'read_unique_id': {
        'cmd1': 0xED,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'block_erase': {
        'cmd1': 0x60,
        'addr_len': 3,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False
    },
    'read_status': {
        'cmd1': 0x70,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'read_status_enhanced': {
        'cmd1': 0x78,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'standard_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True
    },
    'read_cache_sequential': {
        'cmd1': 0x31,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'read_cache_random': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x31,
        'data': None,
        'await_data': True
    },
    'copyback_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x35,
        'data': None,
        'await_data': False
    },
    'copyback_program': {
        'cmd1': 0x85,
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False
    },
    'copyback_read_with_data_output': {
        'cmd1': 0x05,
        'addr_len': 5,
        'cmd2': 0xE0,
        'data': None,
        'await_data': False
    },
    'copyback_program_with_data_mod': {
        'cmd1': 0x85,
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False
    },
    'zq_calibration_long': {
        'cmd1': 0xF9,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'zq_calibration_short': {
        'cmd1': 0xD9,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'set_features': {
        'cmd1': 0xEF,
        'addr_len': 1,
        'cmd2': 0xFA,
        'data': [None, None, None, None],
        'await_data': False
    },
    'get_features': {
        'cmd1': 0xEE,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True
    },
    'set_lun': {
        'cmd1': 0xD5,
        'addr_len': 2,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'get_lun': {
        'cmd1': 0xD4,
        'addr_len': 2,
        'cmd2': None,
        'data': None,
        'await_data': False
    },
    'multi_plane_page_program': {
        'cmd1': 0x80,
        'addr_len': 5,
        'cmd2': 0x11,
        'data': None,
        'await_data': False
    },
    'multi_plane_copyback_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x35,
        'data': None,
        'await_data': False
    },
    'multi_plane_block_erase': {
        'cmd1': 0x60,
        'addr_len': 6,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False
    },
    'multi_plane_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x32,
        'data': None,
        'await_data': True
    }
}
