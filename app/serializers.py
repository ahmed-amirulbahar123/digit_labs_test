from rest_framework import serializers


class LockerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=500, required=False)
    lockerdata = serializers.JSONField()

    def validate_lockerdata(self, value):

        if not isinstance(value, dict):
            raise serializers.ValidationError(
                "lockerdata must be a valid JSON")

        # Check if 'pam' key exists in lockerdata
        if 'pam' not in value:
            raise serializers.ValidationError(
                "Missing 'pam' key in lockerdata")

        pam_data = value['pam']

        # Check if required keys exist in 'pam' data
        required_keys = ['PamUserID', 'pamcredbit', 'PAMConfigurationID']
        missing_keys = [key for key in required_keys if key not in pam_data]
        if missing_keys:
            raise serializers.ValidationError(
                f"Missing required keys in 'pam' data: {', '.join(missing_keys)}")

        # Validate 'port', 'domain', 'database', 'password', and 'username' keys
        for key in ['port', 'domain', 'database', 'password', 'username']:
            if key not in value:
                raise serializers.ValidationError(
                    f"Missing '{key}' key in lockerdata")

        return value


class DefinitionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    detail = serializers.CharField(max_length=500, required=False)
    deftarget = serializers.JSONField()

    def validate_deftarget(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("deftarget must be a valid JSON")

            # Check if 'All' key exists in lockerdata
        if 'All' not in value:
            raise serializers.ValidationError(
                "Missing 'All' key in lockerdata")

        all_data = value['All']

        # Check if 'All' key has nested 'All' key
        if 'All' not in all_data:
            raise serializers.ValidationError(
                "Missing nested 'All' key in lockerdata")

        nested_all_data = all_data['All']

        # Check if 'win' and 'linux' keys exist in nested 'All' data
        required_keys = ['win', 'linux']
        missing_keys = [
            key for key in required_keys if key not in nested_all_data]
        if missing_keys:
            raise serializers.ValidationError(
                f"Missing required keys in nested 'All' data: {', '.join(missing_keys)}")

        # Validate the structure of 'win' and 'linux' data
        for key, data in nested_all_data.items():
            if not isinstance(data, dict):
                raise serializers.ValidationError(
                    f"Value for key '{key}' must be a dictionary")

            for ip, values in data.items():
                if not isinstance(values, list) or 'All' not in values:
                    raise serializers.ValidationError(
                        f"Value for IP '{ip}' under '{key}' must be a list containing 'All'")

        return value
