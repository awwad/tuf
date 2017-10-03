# This file is generated from tuf_asn1_definitions.asn1, by a combination of
# asn1c and asn1ate, along with some hand modification in between.
# After this, the order of components in this file should be hand-modified
# purely for git consistency (readable diffs) and then this sequence of comments
# should be added to the start again.
#
# How to generate this file when changes are made to the ASN.1 definitions in
# tuf_asn1_definitions.asn1:
#
# 1. generate the consolidated ASN.1 definitions in Python using asn1c,
#    putting them in file intermediate_asn1_definitions.asn1:
#    $ asn1c -EF tuf_asn1_definitions.asn1 > intermediate_asn1_definitions.asn1
#
# 2. Make manual edits to the newly generated intermediate_asn1_definitions.asn1
#    to keep it consistent with pyasn1's asn1ate expections:
#
#    2.1 Remove all PATTERN constraints on VisibleString definitions.
#    2.2 Remove extraneous Module definitions: the full file is to be treated
#        as one module.
#        For example, remove sets of three lines like this:
#           END
#           MetadataModule DEFINITIONS AUTOMATIC TAGS ::=
#           BEGIN
#        When you're finished, there should be only one Module definitions
#        statement and one END statement in the file.
#
# 3. Run pyasn1's asn1ate to generate the Python definitions from the
#    consolidated ASN.1 definitions:
#    $ asn1ate intermediate_asn1_definitions.asn1 > metadata_asn1_definitions.py
#
# 4. Add this long comment to the top of the new metadata_asn1_definitions.py.
#
# 5. Finally, if you are committing this to the github repo, please re-order
#    the generated lines to match the previous git version as best you can,
#    so as to avoid junk/unreadable diffs.
#

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful

# To make this module work, had to:
# 1. Define the INTEGER MAX value.
# https://www.obj-sys.com/docs/acv58/CCppUsersGuide/CCppUsersGuidea12.html
MAX = 2**32-1

class OctetString(univ.OctetString):
    pass


OctetString.subtypeSpec = constraint.ValueSizeConstraint(1, 1024)


class EncryptedSymmetricKeyType(univ.Enumerated):
    pass


EncryptedSymmetricKeyType.namedValues = namedval.NamedValues(
    ('aes128', 0),
    ('aes192', 1),
    ('aes256', 2)
)


class EncryptedSymmetricKey(univ.Sequence):
    pass


EncryptedSymmetricKey.componentType = namedtype.NamedTypes(
    namedtype.NamedType('encryptedSymmetricKeyType', EncryptedSymmetricKeyType()),
    namedtype.NamedType('encryptedSymmetricKeyValue', OctetString())
)


class Identifier(char.VisibleString):
    pass


Identifier.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Natural(univ.Integer):
    pass


Natural.subtypeSpec = constraint.ValueRangeConstraint(0, MAX)


class Positive(univ.Integer):
    pass


Positive.subtypeSpec = constraint.ValueRangeConstraint(1, MAX)


class Length(Natural):
    pass


class HashFunction(univ.Enumerated):
    pass


HashFunction.namedValues = namedval.NamedValues(
    ('sha224', 0),
    ('sha256', 1),
    ('sha384', 2),
    ('sha512', 3),
    ('sha512-224', 4),
    ('sha512-256', 5)
)


class Hash(univ.Sequence):
    pass


Hash.componentType = namedtype.NamedTypes(
    namedtype.NamedType('function', HashFunction()),
    namedtype.NamedType('digest', OctetString()))


class Hashes(univ.SequenceOf):
    pass


Hashes.componentType = Hash()
Hashes.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class Filename(char.VisibleString):
    pass


Filename.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Target(univ.Sequence):
    pass


Target.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', Filename()),
    namedtype.NamedType('length', Length()),
    namedtype.NamedType('numberOfHashes', Length()),
    namedtype.NamedType('hashes', Hashes())
)


class Custom(univ.Sequence):
    pass


Custom.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('releaseCounter', Natural()),
    namedtype.OptionalNamedType('hardwareIdentifier', Identifier()),
    namedtype.OptionalNamedType('ecuIdentifier', Identifier()),
    namedtype.OptionalNamedType('encryptedTarget', Target()),
    namedtype.OptionalNamedType('encryptedSymmetricKey', EncryptedSymmetricKey())
)


class Keyid(OctetString):
    pass


class Keyids(univ.SequenceOf):
    pass


Keyids.componentType = Keyid()
Keyids.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class StrictFilename(char.VisibleString):
    pass


StrictFilename.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class RepositoryName(StrictFilename):
    pass


class URL(char.VisibleString):
    pass


URL.subtypeSpec = constraint.ValueSizeConstraint(1, 1024)


class URLs(univ.SequenceOf):
    pass


URLs.componentType = URL()
URLs.subtypeSpec=constraint.ValueSizeConstraint(0, 8)


class Repository(univ.Sequence):
    pass


Repository.componentType = namedtype.NamedTypes(
    namedtype.NamedType('name', RepositoryName()),
    namedtype.NamedType('numberOfServers', Length()),
    namedtype.NamedType('servers', URLs())
)


class Repositories(univ.SequenceOf):
    pass


Repositories.componentType = Repository()
Repositories.subtypeSpec=constraint.ValueSizeConstraint(2, 2)


class Path(char.VisibleString):
    pass


Path.subtypeSpec = constraint.ValueSizeConstraint(1, 32)


class Paths(univ.SequenceOf):
    pass


Paths.componentType = Path()
Paths.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class RepositoryNames(univ.SequenceOf):
    pass


RepositoryNames.componentType = RepositoryName()
RepositoryNames.subtypeSpec=constraint.ValueSizeConstraint(2, 2)


class Mapping(univ.Sequence):
    pass


Mapping.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfPaths', Length()),
    namedtype.NamedType('paths', Paths()),
    namedtype.NamedType('numberOfRepositories', Length()),
    namedtype.NamedType('repositories', RepositoryNames()),
    namedtype.DefaultedNamedType('terminating', univ.Boolean().subtype(value=0))
)


class Mappings(univ.SequenceOf):
    pass


Mappings.componentType = Mapping()
Mappings.subtypeSpec=constraint.ValueSizeConstraint(1, 1)


class MapFile(univ.Sequence):
    pass


MapFile.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfRepositories', Length()),
    namedtype.NamedType('repositories', Repositories()),
    namedtype.NamedType('numberOfMappings', Length()),
    namedtype.NamedType('mappings', Mappings())
)


class SignatureMethod(univ.Enumerated):
    pass


SignatureMethod.namedValues = namedval.NamedValues(
    ('rsassa-pss', 0),
    ('ed25519', 1)
)


class Signature(univ.Sequence):
    pass


Signature.componentType = namedtype.NamedTypes(
    namedtype.NamedType('keyid', Keyid()),
    namedtype.NamedType('method', SignatureMethod()),
    namedtype.NamedType('value', OctetString()))


class Signatures(univ.SequenceOf):
    pass


Signatures.componentType = Signature()
Signatures.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class RoleType(univ.Enumerated):
    pass


RoleType.namedValues = namedval.NamedValues(
    ('root', 0),
    ('targets', 1),
    ('snapshot', 2),
    ('timestamp', 3)
)


class UTCDateTime(Positive):
    pass


# The next class, 'Version', should ideally inherit from class Positive instead
# of Natural; however there is a point during the initial write of metadata
# during which the version may be 0 and signature checks may occur, in which
# case conversions must succeed - so we allow 0 for version, but do not expect
# a version 0 to be final / written to disk / transmitted.
class Version(Natural): # Should be positive, but TUF has a certain point during an initial write during which the version is 0 and signature checks may still occur, in which case conversions must succeed.
    pass


class TargetRoleFileInfo(univ.Sequence):
    pass


TargetRoleFileInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', StrictFilename()),
    namedtype.NamedType('version', Version())
)


class TargetRoleFileInfos(univ.SequenceOf):
    pass


TargetRoleFileInfos.componentType = TargetRoleFileInfo()
TargetRoleFileInfos.subtypeSpec=constraint.ValueSizeConstraint(1, 128)


class RootRoleFileInfo(univ.Sequence):
    pass


RootRoleFileInfo.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', StrictFilename()),
    namedtype.NamedType('version', Version()),
    namedtype.NamedType('length', Length()),
    namedtype.NamedType('numberOfHashes', Length()),
    namedtype.NamedType('hashes', Hashes())
)


class SnapshotMetadata(univ.Sequence):
    pass


SnapshotMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfTargetRoleFiles', Length()),
    namedtype.NamedType('targetRoleFileInfos', TargetRoleFileInfos()),
    namedtype.NamedType('rootRoleFileInfo', RootRoleFileInfo())
)


class PublicKeyType(univ.Enumerated):
    pass


PublicKeyType.namedValues = namedval.NamedValues(
    ('rsa', 0),
    ('ed25519', 1)
)


class PublicKey(univ.Sequence):
    pass


PublicKey.componentType = namedtype.NamedTypes(
    namedtype.NamedType('publicKeyid', Keyid()),
    namedtype.NamedType('publicKeyType', PublicKeyType()),
    namedtype.NamedType('publicKeyValue', OctetString())
)


class PublicKeys(univ.SequenceOf):
    pass


PublicKeys.componentType = PublicKey()
PublicKeys.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class Threshold(Positive):
    pass


class TopLevelRole(univ.Sequence):
    pass


TopLevelRole.componentType = namedtype.NamedTypes(
    namedtype.NamedType('role', RoleType()),
    namedtype.OptionalNamedType('numberOfURLs', Length()),
    namedtype.OptionalNamedType('urls', URLs()),
    namedtype.NamedType('numberOfKeyids', Length()),
    namedtype.NamedType('keyids', Keyids()),
    namedtype.NamedType('threshold', Threshold())
)


class TopLevelRoles(univ.SequenceOf):
    pass


TopLevelRoles.componentType = TopLevelRole()
TopLevelRoles.subtypeSpec=constraint.ValueSizeConstraint(4, 4)


class RootMetadata(univ.Sequence):
    pass


RootMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfKeys', Length()),
    namedtype.NamedType('keys', PublicKeys()),
    namedtype.NamedType('numberOfRoles', Length()),
    namedtype.NamedType('roles', TopLevelRoles())
)


class TimestampMetadata(univ.Sequence):
    pass


TimestampMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('filename', Filename()),
    namedtype.NamedType('version', Version()),
    namedtype.NamedType('length', Length()),
    namedtype.NamedType('numberOfHashes', Length()),
    namedtype.NamedType('hashes', Hashes())
)


class MultiRole(univ.Sequence):
    pass


MultiRole.componentType = namedtype.NamedTypes(
    namedtype.NamedType('rolename', StrictFilename()),
    namedtype.NamedType('numberOfKeyids', Length()),
    namedtype.NamedType('keyids', Keyids()),
    namedtype.NamedType('threshold', Threshold())
)


class MultiRoles(univ.SequenceOf):
    pass


MultiRoles.componentType = MultiRole()
MultiRoles.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class PathsToRoles(univ.Sequence):
    pass


PathsToRoles.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfPaths', Length()),
    namedtype.NamedType('paths', Paths()),
    namedtype.NamedType('numberOfRoles', Length()),
    namedtype.NamedType('roles', MultiRoles()),
    namedtype.DefaultedNamedType('terminating', univ.Boolean().subtype(value=0))
)


class PrioritizedPathsToRoles(univ.SequenceOf):
    pass


PrioritizedPathsToRoles.componentType = PathsToRoles()
PrioritizedPathsToRoles.subtypeSpec=constraint.ValueSizeConstraint(1, 8)


class TargetsDelegations(univ.Sequence):
    pass


TargetsDelegations.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfKeys', Length()),
    namedtype.NamedType('keys', PublicKeys()),
    namedtype.NamedType('numberOfDelegations', Length()),
    namedtype.NamedType('delegations', PrioritizedPathsToRoles())
)


class TargetAndCustom(univ.Sequence):
    pass


TargetAndCustom.componentType = namedtype.NamedTypes(
    namedtype.NamedType('target', Target()),
    namedtype.OptionalNamedType('custom', Custom())
)


class Targets(univ.SequenceOf):
    pass


Targets.componentType = TargetAndCustom()
Targets.subtypeSpec=constraint.ValueSizeConstraint(1, 128)


class TargetsMetadata(univ.Sequence):
    pass


TargetsMetadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('numberOfTargets', Natural()),
    namedtype.NamedType('targets', Targets()),
    namedtype.OptionalNamedType('delegations', TargetsDelegations())
)


class SignedBody(univ.Choice):
    pass


SignedBody.componentType = namedtype.NamedTypes(
    namedtype.NamedType('rootMetadata', RootMetadata()),
    namedtype.NamedType('targetsMetadata', TargetsMetadata()),
    namedtype.NamedType('snapshotMetadata', SnapshotMetadata()),
    namedtype.NamedType('timestampMetadata', TimestampMetadata())
)


class Signed(univ.Sequence):
    pass


Signed.componentType = namedtype.NamedTypes(
    namedtype.NamedType('type', RoleType()),
    namedtype.NamedType('expires', UTCDateTime()),
    # The next field, 'version', should ideally use Positive() instead of
    # Natural(); however there is a point during the initial write of metadata
    # during which the version may be 0 and signature checks may occur, in
    # which case conversions must succeed - so we allow 0 for version, but
    # do not expect a version 0 to be final / written to disk / transmitted.
    namedtype.NamedType('version', Natural()),
    namedtype.NamedType('body', SignedBody())
)


class Metadata(univ.Sequence):
    pass


Metadata.componentType = namedtype.NamedTypes(
    namedtype.NamedType('signed', Signed()),
    namedtype.NamedType('numberOfSignatures', Length()),
    namedtype.NamedType('signatures', Signatures())
)
