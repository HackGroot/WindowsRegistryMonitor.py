import time
import json
import winreg
import logging

class RegistryMonitor:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.keys_to_monitor = self.config['keys_to_monitor']
        self.monitoring_interval = self.config['monitoring_interval']
        
        logging.basicConfig(filename=self.config['log_file'], level=logging.INFO)
        
    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return json.load(file)

    def read_key(self, key, subkey, value_name):
        try:
            with winreg.OpenKey(key, subkey) as reg_key:
                value, _ = winreg.QueryValueEx(reg_key, value_name)
                return value
        except FileNotFoundError:
            return None

    def monitor(self):
        initial_values = {}
        for item in self.keys_to_monitor:
            key = getattr(winreg, item['key'])
            initial_values[item['value_name']] = self.read_key(key, item['subkey'], item['value_name'])

        while True:
            for item in self.keys_to_monitor:
                key = getattr(winreg, item['key'])
                value_name = item['value_name']
                current_value = self.read_key(key, item['subkey'], value_name)
                
                if current_value != initial_values[value_name]:
                    logging.info(f"The registry value '{value_name}' has changed!")
                    initial_values[value_name] = current_value

            time.sleep(self.monitoring_interval)

if __name__ == '__main__':
    monitor = RegistryMonitor('config.json')
    monitor.monitor()
