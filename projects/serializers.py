from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "github", "linkedin", "bio")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        )


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["url", "certificates", "name", "id"]

    def create(self, validated_data):
        certificate_data = validated_data.pop("certificates")

        for certificates in certificate_data:
            certificates[
                "certifying_institution"
            ] = CertifyingInstitution.objects.create(**validated_data)
            CertificateSerializer().create(validated_data=certificates)
        return certificates["certifying_institution"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        ]
