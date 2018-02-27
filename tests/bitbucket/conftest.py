import pytest


@pytest.fixture(scope='function')
def sample_payload_push():
    payload = {
        'eventKey': 'repo:refs_changed',
        'date': '2017-09-19T09:45:32+1000',
        'actor': {
            'name': 'admin',
            'emailAddress': 'admin@example.com',
            'id': 1,
            'displayName': 'Administrator',
            'active': True,
            'slug': 'admin',
            'type': 'NORMAL'
        },
        'repository': {
            'slug': 'repository',
            'id': 84,
            'name': 'repository',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        },
        'changes': [
            {
                'ref': {
                    'id': 'refs/heads/master',
                    'displayId': 'master',
                    'type': 'BRANCH'
                },
                'refId': 'refs/heads/master',
                'fromHash': 'ecddabb624f6f5ba43816f5926e580a5f680a932',
                'toHash': '178864a7d521b6f5e720b386b2c2b0ef8563e0dc',
                'type': 'UPDATE'
            }
        ]
    }
    return payload


@pytest.fixture(scope='function')
def sample_payload_modified():
    payload = {
        'eventKey': 'repo:modified',
        'date': '2017-09-19T09:51:20+1000',
        'actor': {
            'name': 'admin',
            'emailAddress': 'admin@example.com',
            'id': 1,
            'displayName': 'Administrator',
            'active': True,
            'slug': 'admin',
            'type': 'NORMAL'
        },
        'old': {
            'slug': 'repository',
            'id': 84,
            'name': 'repository',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        },
        'new': {
            'slug': 'repository2',
            'id': 84,
            'name': 'repository2',
            'scmId': 'git',
            'state': 'AVAILABLE',
            'statusMessage': 'Available',
            'forkable': True,
            'project': {
                'key': 'PROJ',
                'id': 84,
                'name': 'project',
                'public': False,
                'type': 'NORMAL'
            },
            'public': False
        }
    }
    return payload

def your_mother(foo,bar):
    return foo, bar

@pytest.fixture(scope='function')
def minion_mock(mocker):
    minion = mocker.patch('salt.minion.SMinion', autospec=True)
    minion.return_value.functions = {'event.send': your_mother}
    return minion

@pytest.fixture(scope='function')
def client_caller(mocker):
    expected_calls = [mocker.call(
        {'interface': '0.0.0.0', 'master': 'salt', 'master_type': 'str', 'master_uri_format': 'default',
         'master_port': 4506, 'master_finger': '', 'master_shuffle': False, 'master_alive_interval': 0,
         'master_failback': False, 'master_failback_interval': 0, 'verify_master_pubkey_sign': False,
         'sign_pub_messages': False, 'always_verify_signature': False, 'master_sign_key_name': 'master_sign',
         'syndic_finger': '', 'user': 'sschweer', 'root_dir': '/', 'pki_dir': '/etc/salt/pki/minion', 'id': 'bart',
         'cachedir': '/var/cache/salt/minion', 'append_minionid_config_dirs': [], 'cache_jobs': False,
         'grains_cache': False, 'grains_cache_expiration': 300, 'grains_deep_merge': False,
         'conf_file': '/etc/salt/minion', 'sock_dir': '/var/run/salt/minion', 'sock_pool_size': 1, 'backup_mode': '',
         'renderer': 'yaml_jinja', 'renderer_whitelist': [], 'renderer_blacklist': [], 'random_startup_delay': 0,
         'failhard': False, 'autoload_dynamic_modules': True, 'environment': None, 'pillarenv': None,
         'pillarenv_from_saltenv': False, 'pillar_opts': False, 'pillar_cache': False, 'pillar_cache_ttl': 3600,
         'pillar_cache_backend': 'disk', 'extension_modules': '/var/cache/salt/minion/extmods', 'state_top': 'top.sls',
         'state_top_saltenv': None, 'startup_states': '', 'sls_list': [], 'top_file': '', 'thorium_interval': 0.5,
         'thorium_roots': {'base': ['/srv/thorium']}, 'file_client': 'remote', 'local': False,
         'use_master_when_local': False, 'file_roots': {'base': ['/srv/salt', '/srv/spm/salt']},
         'top_file_merging_strategy': 'merge', 'env_order': [], 'default_top': 'base',
         'fileserver_limit_traversal': False, 'file_recv': False, 'file_recv_max_size': 100, 'file_ignore_regex': [],
         'file_ignore_glob': [], 'fileserver_backend': ['roots'], 'fileserver_followsymlinks': True,
         'fileserver_ignoresymlinks': False, 'pillar_roots': {'base': ['/srv/pillar', '/srv/spm/pillar']},
         'on_demand_ext_pillar': ['libvirt', 'virtkey'], 'decrypt_pillar': [], 'decrypt_pillar_delimiter': ':',
         'decrypt_pillar_default': 'gpg', 'decrypt_pillar_renderers': ['gpg'], 'git_pillar_base': 'master',
         'git_pillar_branch': 'master', 'git_pillar_env': '', 'git_pillar_root': '', 'git_pillar_ssl_verify': True,
         'git_pillar_global_lock': True, 'git_pillar_user': '', 'git_pillar_password': '',
         'git_pillar_insecure_auth': False, 'git_pillar_privkey': '', 'git_pillar_pubkey': '',
         'git_pillar_passphrase': '',
         'git_pillar_refspecs': ['+refs/heads/*:refs/remotes/origin/*', '+refs/tags/*:refs/tags/*'],
         'git_pillar_includes': True, 'gitfs_remotes': [], 'gitfs_mountpoint': '', 'gitfs_root': '',
         'gitfs_base': 'master', 'gitfs_user': '', 'gitfs_password': '', 'gitfs_insecure_auth': False,
         'gitfs_privkey': '', 'gitfs_pubkey': '', 'gitfs_passphrase': '', 'gitfs_env_whitelist': [],
         'gitfs_env_blacklist': [], 'gitfs_global_lock': True, 'gitfs_ssl_verify': True, 'gitfs_saltenv': [],
         'gitfs_refspecs': ['+refs/heads/*:refs/remotes/origin/*', '+refs/tags/*:refs/tags/*'], 'hash_type': 'sha256',
         'disable_modules': [], 'disable_returners': [], 'whitelist_modules': [], 'module_dirs': [],
         'returner_dirs': [], 'grains_dirs': [], 'states_dirs': [], 'render_dirs': [], 'outputter_dirs': [],
         'utils_dirs': ['/var/cache/salt/minion/extmods/utils'], 'publisher_acl': {}, 'publisher_acl_blacklist': {},
         'providers': {}, 'clean_dynamic_modules': True, 'open_mode': False, 'auto_accept': True,
         'autosign_timeout': 120, 'multiprocessing': True, 'mine_enabled': True, 'mine_return_job': False,
         'mine_interval': 60, 'ipc_mode': 'ipc', 'ipc_write_buffer': 0, 'ipv6': None, 'file_buffer_size': 262144,
         'tcp_pub_port': 4510, 'tcp_pull_port': 4511, 'tcp_authentication_retries': 5,
         'log_file': '/var/log/salt/minion', 'log_level': 'warning', 'log_level_logfile': None,
         'log_datefmt': '%H:%M:%S', 'log_datefmt_logfile': '%Y-%m-%d %H:%M:%S',
         'log_fmt_console': '[%(levelname)-8s] %(message)s',
         'log_fmt_logfile': '%(asctime)s,%(msecs)03d [%(name)-17s:%(lineno)-4d][%(levelname)-8s][%(process)d] %(message)s',
         'log_granular_levels': {}, 'log_rotate_max_bytes': 0, 'log_rotate_backup_count': 0, 'max_event_size': 1048576,
         'test': False, 'ext_job_cache': '', 'cython_enable': False, 'enable_zip_modules': False, 'state_verbose': True,
         'state_output': 'full', 'state_output_diff': False, 'state_auto_order': True, 'state_events': False,
         'state_aggregate': False, 'snapper_states': False, 'snapper_states_config': 'root', 'acceptance_wait_time': 10,
         'acceptance_wait_time_max': 0, 'rejected_retry': False, 'loop_interval': 1, 'verify_env': True, 'grains': {},
         'permissive_pki_access': False, 'default_include': 'minion.d/*.conf', 'update_url': False,
         'update_restart_services': [], 'retry_dns': 30, 'resolve_dns_fallback': True, 'recon_max': 10000,
         'recon_default': 1000, 'recon_randomize': True, 'return_retry_timer': 5, 'return_retry_timer_max': 10,
         'random_reauth_delay': 10, 'winrepo_source_dir': 'salt://win/repo-ng/', 'winrepo_dir': '/srv/salt/win/repo',
         'winrepo_dir_ng': '/srv/salt/win/repo-ng', 'winrepo_cachefile': 'winrepo.p', 'winrepo_cache_expire_max': 21600,
         'winrepo_cache_expire_min': 0, 'winrepo_remotes': ['https://github.com/saltstack/salt-winrepo.git'],
         'winrepo_remotes_ng': ['https://github.com/saltstack/salt-winrepo-ng.git'], 'winrepo_branch': 'master',
         'winrepo_ssl_verify': True, 'winrepo_user': '', 'winrepo_password': '', 'winrepo_insecure_auth': False,
         'winrepo_privkey': '', 'winrepo_pubkey': '', 'winrepo_passphrase': '',
         'winrepo_refspecs': ['+refs/heads/*:refs/remotes/origin/*', '+refs/tags/*:refs/tags/*'],
         'pidfile': '/var/run/salt-minion.pid', 'range_server': 'range:80', 'reactor_refresh_interval': 60,
         'reactor_worker_threads': 10, 'reactor_worker_hwm': 10000, 'engines': [], 'tcp_keepalive': True,
         'tcp_keepalive_idle': 300, 'tcp_keepalive_cnt': -1, 'tcp_keepalive_intvl': -1, 'modules_max_memory': -1,
         'grains_refresh_every': 0, 'minion_id_caching': True, 'keysize': 2048, 'transport': 'zeromq',
         'auth_timeout': 5, 'auth_tries': 7, 'master_tries': 1, 'auth_safemode': False, 'random_master': False,
         'minion_floscript': '/home/sschweer/Projects/muffineer/.venv/lib/python3.6/site-packages/salt-2017.7.4-py3.6.egg/salt/daemons/flo/minion.flo',
         'caller_floscript': '/home/sschweer/Projects/muffineer/.venv/lib/python3.6/site-packages/salt-2017.7.4-py3.6.egg/salt/daemons/flo/caller.flo',
         'ioflo_verbose': 0, 'ioflo_period': 0.1, 'ioflo_realtime': True, 'ioflo_console_logdir': '', 'raet_port': 4510,
         'raet_alt_port': 4511, 'raet_mutable': False, 'raet_main': False, 'raet_clear_remotes': True,
         'raet_clear_remote_masters': True, 'raet_road_bufcnt': 2, 'raet_lane_bufcnt': 100, 'cluster_mode': False,
         'cluster_masters': [], 'restart_on_error': False, 'ping_interval': 0, 'username': None, 'password': None,
         'zmq_filtering': False, 'zmq_monitor': False, 'cache_sreqs': True, 'cmd_safe': True, 'sudo_user': '',
         'http_request_timeout': 3600.0, 'http_max_body': 107374182400, 'event_match_type': 'startswith',
         'minion_restart_command': [], 'pub_ret': True, 'proxy_host': '', 'proxy_username': '', 'proxy_password': '',
         'proxy_port': 0, 'minion_jid_queue_hwm': 100, 'ssl': None, 'multifunc_ordered': False,
         'beacons_before_connect': False, 'scheduler_before_connect': False, 'cache': 'localfs',
         'salt_cp_chunk_size': 65536, 'extmod_whitelist': {}, 'extmod_blacklist': {}, 'minion_sign_messages': False,
         'schedule': {}, '__role': 'minion', '__cli': 'pytest', 'beacons': {}})]
    return expected_calls
