import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_cronjob_exists(File):
    f = File('/etc/cron.daily/certbot-renew')
    assert f.is_file
